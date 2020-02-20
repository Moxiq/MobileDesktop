package com.example.streamdesktop;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;

import com.example.streamdesktop.Mjpeg.MjpegInputStream;
import com.example.streamdesktop.Mjpeg.MjpegView;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;


public class ConnectedActivity extends Activity {
    private String url = "http://192.168.0.34:5000/video_feed";
    private MjpegView mv;
    private Connection con;
    private final BlockingQueue<String> inputBuf = new LinkedBlockingQueue<String>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_connected);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        mv = (MjpegView) findViewById(R.id.mjpegview);

        con = new Connection("192.168.0.34", 10000);
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
    }


}
