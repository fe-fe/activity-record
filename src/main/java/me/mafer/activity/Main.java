/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package me.mafer.activity;

/**
 *
 * @author fefe
 */
public class Main {

    public static void main(String[] args) {
        
        ActivityRecorder.setCurrentNature(SessionNature.ACADEMIC);
        
        Subject javaSubject = Subject.addNewSubject("Java");
        javaSubject.addAlias("NetBeans");
        javaSubject.addAlias("IntelliJ");
        
        Subject.addNewSubject("FireFox");
        
        ActivityRecorder recorder = new ActivityRecorder();
        
        recorder.start();
    }
}