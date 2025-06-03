/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package me.mafer.activity;

import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 *
 * @author fefe
 */
public class Subject {
    
    private final static Set<Subject> subjects = Collections.synchronizedSet(new HashSet<>());
    
    private final String name;
    private Set<String> aliases;
    
    private Subject(String name) {
        this.name = name;
        this.aliases = new HashSet<>();
    }
    
    public static Subject addNewSubject(String name) {
        Subject newSubject = new Subject(name);
        newSubject.addAlias(name);
        subjects.add(newSubject);
        return newSubject;
    }
    
    private boolean isSubjectInTitle(String title) {
        for (String alias : this.aliases) {
            if (title.toLowerCase().contains(alias.toLowerCase())) {
                return true;
            }
        }
        return false;
    }
    
    public static Set<Subject> getSubjectsInTitle(String title) {
        Set<Subject> presentSubjects = new HashSet<>();
        for (Subject subject : subjects) {
            if (subject.isSubjectInTitle(title)) {
                presentSubjects.add(subject);
            }
        }
        return presentSubjects;
    }
    
    @Override
    public String toString() {
        return "\nSubject Found: " + name + " Aliases: " + aliases.toString();
    }
    
    public void addAlias(String alias) {
        this.aliases.add(alias);
    } 
    
    public void removeAlias(String alias) {
        this.aliases.remove(alias);
    }
    
    public String getName() {
        return name;
    }
}