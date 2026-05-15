package com.github.alexmovsess.practice.AdventOfCode2016.Day4;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AoC2016_Day4 {
    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day4.class.getResourceAsStream("AoC2016_Day4_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int result = 0;
            while (sc.hasNext()){
                String input = sc.next();
                Pattern pattern = Pattern.compile("(.+)-(\\d+)\\[(\\w+)\\]", Pattern.CASE_INSENSITIVE);
                Matcher matcher = pattern.matcher(input);
                if (matcher.find()){
                    
                    String[] roomName = matcher.group(1).split("-");
                    int sectorID = Integer.parseInt(matcher.group(2));
                    String checksum = matcher.group(3);
                    String fullRoomName = "";
                    for (String str : roomName) { 
                        fullRoomName+=str;
                    }

                    Map<Character, Integer> sortedMap = getOccurringCharMap(fullRoomName);
    
                    if (keyEqualsString(sortedMap.keySet(), checksum)){
                        result+=sectorID;
                    }
                }
            }
            return Integer.toString(result);
        }
    }

    static Boolean keyEqualsString(Set<Character> set, String str){
        //Compares a set of character to a string. Returns true if every character is in the string in order, else false. Set and String must be same length.
        int i = 0;

        for (Character key : set) {
            if (key == str.charAt(i)){
                i+=1;
            }else{
                return false;
            }
        }

        return true;
    }

    static Map<Character, Integer> getOccurringCharMap(String str)
    //Returns a Map of every Char in a string with their number of occurences.
    {
        Map<Character, Integer> charMap = new HashMap<Character, Integer>();
        int len = str.length();
        for (int i = 0; i < len; i++) {
            char thisChar = str.charAt(i);
            charMap.computeIfPresent(thisChar, (k, v) -> v+=1);
            charMap.computeIfAbsent(thisChar, k -> 1);
        }
        Map<Character, Integer> sortedMap = sortMap(charMap, true);
        return sortedMap;
    }

    public static Map<Character, Integer> sortMap(Map<Character, Integer> map, Boolean reverseOrder) {
        //Returns a sorted map of size 5 sorted by value and then by alphabetical order of key for ties.
        List<Entry<Character, Integer>> list = new ArrayList<>(map.entrySet());

        list.sort(Collections.reverseOrder(Entry.comparingByValue())); //Sorts by value the entire map

        Map<Character, Integer> fullSortedMap = new LinkedHashMap<>();
        Map<Character, Integer> sortedMap = new LinkedHashMap<>();
        int i = 0;

        while(i<list.size()-1){ //Sorts the ties by alphabetical order
            int currentValue = list.get(i).getValue();
            Map<Character, Integer> sortedSubMap = new TreeMap<>();
            
            sortedSubMap.put(list.get(i).getKey(), list.get(i).getValue());

            while (list.get(i+1).getValue() == currentValue && i<list.size()-2){
                i+=1;
                sortedSubMap.put(list.get(i).getKey(), list.get(i).getValue());
            }

            if (i==list.size()-2){
                sortedSubMap.put(list.get(i+1).getKey(), list.get(i+1).getValue());
            }

            for (Map.Entry<Character, Integer> entry : sortedSubMap.entrySet()) {
                fullSortedMap.put(entry.getKey(), entry.getValue());
            }
            i+=1;
        }

        List<Entry<Character, Integer>> fullSortedlist = new ArrayList<>(fullSortedMap.entrySet());
        for (Map.Entry<Character, Integer> entry : fullSortedlist.subList(0, 5)) {//Cut the map to first five entries
            sortedMap.put(entry.getKey(), entry.getValue());
        }
        return sortedMap;
    }

    @SuppressWarnings("resource")
    public static String Problem2(){
        InputStream inputStream = AoC2016_Day4.class.getResourceAsStream("AoC2016_Day4_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            while (sc.hasNext()){
                String input = sc.next();
                Pattern pattern = Pattern.compile("(.+)-(\\d+)\\[(\\w+)\\]", Pattern.CASE_INSENSITIVE);
                Matcher matcher = pattern.matcher(input);
                if (matcher.find()){
                    
                    String roomName = String.join(" ", matcher.group(1).split("-"));
                    int sectorID = Integer.parseInt(matcher.group(2));

                    if(caesarSolve(roomName,sectorID).equals("northpole object storage")){
                        return Integer.toString(sectorID);
                    }
                }
            }
        }
        return "error";
    }

    static String caesarSolve(String roomName, int sectorId){
        int len = roomName.length();
        String result = "";
        for (int i = 0; i < len; i++) {
            int asciiCharValue = (int) roomName.charAt(i);
            if (asciiCharValue != 32){
                asciiCharValue += sectorId;
                while(asciiCharValue>122){
                    asciiCharValue-= 26;
                }
                result += (char) asciiCharValue;
            }
            else{
                result += " ";
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+Problem1());
        System.out.println("Problem2 Solution : "+Problem2());
    }   
}
