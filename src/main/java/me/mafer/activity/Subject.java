/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package me.mafer.activity;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.regex.Pattern;
import java.util.Set;

/**
 *
 * @author fefe
 */
public class Subject {
    
    private final static List<Subject> subjects = Collections.synchronizedList(new ArrayList<>());
    
    private final String name;
    private final Set<String> aliases;
    private Pattern regexPattern;
    
    private Subject(String name) {
        this.name = name;
        this.aliases = new HashSet<>();
    }
    
    public static Subject addNewSubject(String name) {
        Subject newSubject = new Subject(name);
        newSubject.addAlias(name);
        newSubject.generateRegexPattern();
        subjects.add(newSubject);
        return newSubject;
    }
    
    private boolean isSubjectInTitle(String title) {
        return regexPattern.matcher(title).find();
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
        aliases.add(alias);
        generateRegexPattern();
        
    } 
    
    public void removeAlias(String alias) {
        aliases.remove(alias);
    }
    
    public String getName() {
        return name;
    }
    
    public void generateRegexPattern() {
        if (aliases == null || aliases.isEmpty()) {
            return;
        }

        StringBuilder newRegexPattern = new StringBuilder();
        newRegexPattern.append("(?:^|[ .-_])(");

        ArrayList<String> aliasesArray = new ArrayList<>(aliases);

        for (int i = 0; i < aliasesArray.size(); i++) {
            newRegexPattern.append(Pattern.quote(aliasesArray.get(i)));
            if (i < aliasesArray.size() - 1) {
                newRegexPattern.append("|");
            }
        }

        newRegexPattern.append(")(?:$|[ .:-_,])");
        
        this.regexPattern = Pattern.compile(newRegexPattern.toString(), Pattern.CASE_INSENSITIVE);
    }
}