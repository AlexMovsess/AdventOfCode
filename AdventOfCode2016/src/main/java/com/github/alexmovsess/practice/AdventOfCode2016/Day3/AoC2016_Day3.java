package com.github.alexmovsess.practice.AdventOfCode2016.Day3;

import java.io.InputStream;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AoC2016_Day3 {

    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day3.class.getResourceAsStream("AoC2016_Day3_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int result = 0;
            while (sc.hasNext()){
                String input = sc.next();
                Pattern pattern = Pattern.compile("(\\d+)\\D+(\\d+)\\D+(\\d+)", Pattern.CASE_INSENSITIVE);
                Matcher matcher = pattern.matcher(input);
                if (matcher.find()){
                    
                    int sideB = Integer.parseInt(matcher.group(1));
                    int sideA = Integer.parseInt(matcher.group(2));
                    int sideC = Integer.parseInt(matcher.group(3));
                    if (sideA + sideB > sideC && sideA + sideC > sideB && sideB + sideC > sideA){
                        result +=1;
                    }
                }
            }
            return Integer.toString(result);
        }
    }

    public static String Problem2()
    {
        InputStream inputStream = AoC2016_Day3.class.getResourceAsStream("AoC2016_Day3_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int result = 0;
            while (sc.hasNext()){
                String input1 = sc.next();
                String input2 = sc.next();
                String input3 = sc.next();
                Pattern pattern = Pattern.compile("(\\d+)\\D+(\\d+)\\D+(\\d+)", Pattern.CASE_INSENSITIVE);
                Matcher matcher1 = pattern.matcher(input1);
                Matcher matcher2 = pattern.matcher(input2);
                Matcher matcher3 = pattern.matcher(input3);
                if (matcher1.find() && matcher2.find() && matcher3.find()){
                    
                    for (int i =1;i <4;i++){
                        int sideB = Integer.parseInt(matcher1.group(i));
                        int sideA = Integer.parseInt(matcher2.group(i));
                        int sideC = Integer.parseInt(matcher3.group(i));

                        if (sideA + sideB > sideC && sideA + sideC > sideB && sideB + sideC > sideA){
                            result +=1;
                        }
                    }

                }
            }
            return Integer.toString(result);
        }
    }

    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+Problem1());
        System.out.println("Problem2 Solution : "+Problem2());
    }   
}

