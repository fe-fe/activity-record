/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package me.mafer.activity;

import java.util.Set;

/**
 *
 * @author fefe
 */
public class ActivityRecorder extends Thread {
    private static SessionNature currentNature;
    private static boolean isRunning = true;
    
    public static SessionNature getCurrentNature() {
        return currentNature;
    }
    
    public static void setCurrentNature(SessionNature nature) {
        currentNature = nature;
    }
    
    @Override
    public void run() {
        while(isRunning) {
            long startTime = System.currentTimeMillis();
            String currentTitle = WindowTitleFetcher.getActiveWindowTitle();
            
            while (WindowTitleFetcher.getActiveWindowTitle().equals(currentTitle)) {
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    System.out.println(e.getMessage());
                }
            }
            
            if (!currentTitle.isEmpty()) {
                long elapsedTime = System.currentTimeMillis() - startTime;
                Set<Subject> subjects = Subject.getSubjectsInTitle(currentTitle);
                if (!subjects.isEmpty()) {
                    for (Subject subject : subjects) {
                        Session session = Session.getMatchingActiveSession(subject);
                        session.sumElapsedTime(elapsedTime);
                        System.out.println(session);
                    }
                }
            }
        }
    }
}