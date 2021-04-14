package com.company;

import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class Main {
    public static void main(String[] args) {
        connection con = new connection("cRF2dvDZQsmu37WGgK6MTcL7XjH");

        try {
            String ret = con.Get();
            System.out.println(ret);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}


class connection{

    HttpsURLConnection con;
    static String auth = "Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI";

    public connection(String id){
        URL url = null;

        try {
            url = new URL("https://eluv.io/items/"+id);
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }

        try {
            this.con = (HttpsURLConnection) url.openConnection();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            this.con.setRequestMethod("GET");
        } catch (ProtocolException e) {
            e.printStackTrace();
        }

        this.con.setRequestProperty("Authorization", auth);
        this.con.setConnectTimeout(5000);
    }

    public String Get() throws IOException {
        int status = this.con.getResponseCode();

        BufferedReader in = new BufferedReader(
                new InputStreamReader(this.con.getInputStream()));
        String inputLine;
        StringBuffer content = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();

        return content.toString();
    }
}