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
        System.out.println("os.name = " + System.getProperty("os.name"));
        
        ActivityRecorder.setCurrentNature(SessionNature.ACADEMIC);
        
        Subject javaSubject = Subject.addNewSubject("Java");
        javaSubject.addAlias("NetBeans");
        javaSubject.addAlias("IntelliJ");
        
        Subject.addNewSubject("FireFox");
        
        ActivityRecorder recorder = new ActivityRecorder();
        
        recorder.run();
        
        System.out.println("Comecou!!!");
    }
}
