/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package me.mafer.activity;

import com.sun.jna.Native;
import com.sun.jna.platform.win32.User32;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import com.sun.jna.platform.win32.WinDef.HWND;

/**
 *
 * @author fefe
 */
public class WindowTitleFetcher {
    private static final String osName = System.getProperty("os.name");
    
    public static String getActiveWindowTitle() {
        switch (osName) {
            case "Linux":
                return getLinuxActiveWindowTitle();
            case "Windows 10":
                return getWindowsActiveWindowTitle();
            default:
                return "unsupported os";      
        }
    }
    
    private static String getLinuxActiveWindowTitle() {
        final String[] command = new String[] {"/bin/bash", "-c", "xprop -id $(xprop -root 32x '\\t$0' _NET_ACTIVE_WINDOW | cut -f 2) _NET_WM_NAME"};
        try {
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            Process process = processBuilder.start();
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream())
            );
            try {
                String[] title = reader.readLine().split("\"");
                return title[1];
            } catch (NullPointerException e) {
                return "";
            }
            
            
            
        } catch (IOException e) {
            return e.getMessage();
        }
    }
    
    private static String getWindowsActiveWindowTitle() {
        HWND hwnd = User32.INSTANCE.GetForegroundWindow();
        char[] buffer = new char[512];
        User32.INSTANCE.GetWindowText(hwnd, buffer, 512);
        String title = Native.toString(buffer);
        return title;
    }
}
