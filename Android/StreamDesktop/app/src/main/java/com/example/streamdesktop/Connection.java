package com.example.streamdesktop;
import android.os.AsyncTask;
import android.util.Log;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class Connection {
    private String host;
    private int port;
    private Socket socket;
    private Boolean isConnected = null;
    private Object syncObject;
    private final BlockingQueue<String> inputBuf = new LinkedBlockingQueue<String>();
    private SendDataTask sendTask;

    public Connection(String host, int port) {
        this.host = host;
        this.port = port;
    }

    //Waits for a connection to be made or fail.
    public boolean requestConnection() {
        syncObject = new Object();
        new StartConnectionTask().execute();
        synchronized (syncObject) {
            try {
                syncObject.wait();
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        return isConnected;
    }

    public void sendString(String data) {
        if (sendTask == null) {
            sendTask = new SendDataTask();
            sendTask.execute();
        }
        inputBuf.add(data);
    }

    public void disconnect() {
        try {
            this.socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    class StartConnectionTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            if (socket == null) {
                synchronized (syncObject) {
                    try {
                        socket = new Socket();
                        socket.connect(new InetSocketAddress(host, port), 5000);
                        isConnected = true;
                        syncObject.notify();
                    } catch (IOException e) {  // Might want to check for interruptedexception here
                        isConnected = false;
                        syncObject.notify();
                    }
                }
            }
            return null;
        }
    }

    class SendDataTask extends AsyncTask<String, Void, Void> {
        OutputStreamWriter writer;

        @Override
        protected Void doInBackground(String... arg0) {
            String data;
            try {
                writer = new OutputStreamWriter(socket.getOutputStream(), "UTF-8");
            } catch (IOException e) {
                e.printStackTrace();
            }
            while (socket.isConnected()) {
                try {
                    data = inputBuf.take();
                    writer.write(data, 0, data.length());
                    writer.flush();
                } catch (InterruptedException | IOException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }
    }
}
