package com.github.alexmovsess.practice.AdventOfCode2016.Day11;

import java.io.InputStream;
import java.util.Objects;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AoC2016_Day11 {

    public static String Problem1()
    {

        InputStream inputStream = AoC2016_Day11.class.getResourceAsStream("AoC2016_Day11_input.txt");
        int result = 0;
        String[][] floorMatrix = new String[4][10];

        System.out.println(floorMatrix.toString());
        
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {

            while (sc.hasNext()){

                String input = sc.next();
                
                Pattern pattern = Pattern.compile("(\\w+) generator|(\\w+)-compatible microchip");
                Matcher matcher = pattern.matcher(input);

                while (matcher.find()){

                    String group1 = matcher.group(1);
                    
                    String group2 = matcher.group(2);

                    if(Objects.nonNull(group1)){
                        
                    }

                }

            }

        }

        return Integer.toString(result);

    }

    public static void main(String[] args) 
    {
        
        System.out.println("Problem1 Solution : "+ Problem1());
        // System.out.println("Problem2 Solution : "+ Problem2());

    }
    
}
