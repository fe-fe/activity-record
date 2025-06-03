/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package me.mafer.activity;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

/**
 *
 * @author fefe
 */
public class Session {
    // synchronizedList makes that the object is locked while a thread is accessing it, so that no other thread can access or modify it
    private final static Set<Session> sessions = Collections.synchronizedSet(new HashSet<>());
    
    private final Subject subject;
    private final LocalDate date;
    private long elapsedTime;
    private final SessionNature nature;

    
    private Session(Subject subject) {
        this.subject = subject;
        this.nature = ActivityRecorder.getCurrentNature();
        this.date = LocalDate.now();
        this.elapsedTime = 0;
    }
    
    public static Session getMatchingActiveSession(Subject subject) {
        
        for (Session session : sessions) {
            
            boolean sameNature = session.getNature().equals(ActivityRecorder.getCurrentNature());
            boolean sameSubject = session.getSubject().equals(subject);
            boolean sameDate = session.getDate().equals(LocalDate.now());
            
            if (sameNature && sameSubject && sameDate) {
                return session;
            }
        }
        Session session = new Session(subject);
        sessions.add(session);
        return session;
    }
    
    public void sumElapsedTime(long elapsedTime) {
        this.elapsedTime += elapsedTime / 1000;
    }
    
    public Subject getSubject() {
        return subject;
    }

    public LocalDate getDate() {
        return date;
    }

    public long getTimeElapsed() {
        return elapsedTime;
    }
    
    public SessionNature getNature() {
        return nature;
    }
    
    @Override
    public String toString() {
        return "Subject Name: " + subject.getName() + "\nNature: " + nature.name() + "\nElapsed Time: " + elapsedTime;
    }
    
}
