package com.github.alexmovsess.practice.AdventOfCode2016.Day6;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class AoC2016_Day6 {
    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day6.class.getResourceAsStream("AoC2016_Day6_input.txt");
        String result = "";
        ArrayList<HashMap<Character, Integer>> columnList = new ArrayList<>();
        for (int i =0; i<8; i++){
            columnList.add(new HashMap<>());
        }
        try (Scanner sc = new Scanner(inputStream)) {
            while (sc.hasNext()){
                String input = sc.next();
                for (int i = 0; i < input.length(); i++){
                    char c = input.charAt(i);        
                    if (columnList.get(i).containsKey(c)) {
                        columnList.get(i).put(c, columnList.get(i).get(c) + 1);
                    } else {
                        columnList.get(i).put(c,1);
                    }
                }
            }
        for (int i = 0; i < columnList.size(); i++) {
            Map<Character, Integer> element = sortByValue(columnList.get(i), true);
            result += element.keySet().toArray()[0];            
        }
        return result;
        }
        
    }

    public static <K, V extends Comparable<? super V>> Map<K, V> sortByValue(Map<K, V> map, Boolean desc) {
        //Sorts a map using its values. Ascending if desc == False, else descending.
        List<Entry<K, V>> list = new ArrayList<>(map.entrySet());
        if (desc){
            list.sort(Collections.reverseOrder(Entry.comparingByValue()));
        }else{
            list.sort(Entry.comparingByValue());
        }

        Map<K, V> result = new LinkedHashMap<>();
        for (Entry<K, V> entry : list) {
            result.put(entry.getKey(), entry.getValue());
        }

        return result;
    }


    public static String Problem2()
    {
        InputStream inputStream = AoC2016_Day6.class.getResourceAsStream("AoC2016_Day6_input.txt");
        String result = "";
        ArrayList<HashMap<Character, Integer>> columnList = new ArrayList<>();
        for (int i =0; i<8; i++){
            columnList.add(new HashMap<>());
        }
        try (Scanner sc = new Scanner(inputStream)) {
            while (sc.hasNext()){
                String input = sc.next();
                for (int i = 0; i < input.length(); i++){
                    char c = input.charAt(i);        
                    if (columnList.get(i).containsKey(c)) {
                        columnList.get(i).put(c, columnList.get(i).get(c) + 1);
                    } else {
                        columnList.get(i).put(c,1);
                    }
                }
            }
        for (int i = 0; i < columnList.size(); i++) {
            Map<Character, Integer> element = sortByValue(columnList.get(i), false);
            result += element.keySet().toArray()[0];            
        }
        return result;
        }
        
    }

    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+ Problem1());
        System.out.println("Problem2 Solution : "+ Problem2());
    }      
}
