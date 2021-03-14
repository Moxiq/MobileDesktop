package com.example.streamdesktop;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.StrictMode;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.widget.ImageView;

import com.example.streamdesktop.Mjpeg.MjpegInputStream;
import com.example.streamdesktop.Mjpeg.MjpegView;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;


public class ConnectedActivity extends Activity {
    private SharedPreferences sp;
    private String hostIp;
    private String hostPort;
    private String url;
    private MjpegView mv;
    private Connection con;

    private ImageView imgDesk;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connected);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        SharedPreferences sp = PreferenceManager.getDefaultSharedPreferences(this.getApplicationContext());
        this.hostIp = sp.getString("hostIP", "192.168.0.33");
        this.hostPort = sp.getString("hostPort", "5034");
        this.url = String.format("http://%s:%s/video_feed", hostIp, hostPort);

        mv = (MjpegView) findViewById(R.id.mjpegview);
        imgDesk = (ImageView) findViewById(R.id.img_desk);


        con = new Connection(this.hostIp, 10000);
        if (con.requestConnection()) {
            mv.setDisplayMode(MjpegView.SIZE_BEST_FIT);
            mv.showFps(false);
            mv.setSource(MjpegInputStream.read(url));
        }
        else {
            AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(ConnectedActivity.this);
            alertDialogBuilder.setTitle("Connection Status");
            alertDialogBuilder.setMessage("Connection failed! Please try again").setCancelable(false);
            alertDialogBuilder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    dialog.cancel();
                    finish();
                }
            });
            AlertDialog alertDialog = alertDialogBuilder.create();
            alertDialog.show();

        }


        mv.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                int x = (int)((motionEvent.getX() / mv.getWidth()) * 100);
                int y = (int)((motionEvent.getY() / mv.getHeight()) * 100);
                con.sendString(x + "," + y);
                //con.sendString((int)mv.getWidth() + "," + (int)mv.getHeight());
                return false;
            }
        });

        imgDesk.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                con.sendString("100,100");
            }
        });
    }


}
