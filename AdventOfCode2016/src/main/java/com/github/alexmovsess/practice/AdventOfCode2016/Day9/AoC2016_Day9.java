package com.github.alexmovsess.practice.AdventOfCode2016.Day9;

import java.io.InputStream;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.LinkedList;
import java.util.Queue;
import org.javatuples.*;

public class AoC2016_Day9 {

    public static String Problem1()
    {

        InputStream inputStream = AoC2016_Day9.class.getResourceAsStream("AoC2016_Day9_input.txt");
        int result = 0;

        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {

            String input = sc.next();
            
            Pattern pattern = Pattern.compile("(^.*?)\\((\\d+)x(\\d+)\\)(.+)");
            Matcher matcher = pattern.matcher(input);

            while (matcher.find()){
                
                String textBeforePattern = matcher.group(1);
                int repeatLength = Integer.parseInt(matcher.group(2));
                int repeatNumber = Integer.parseInt(matcher.group(3));                
                input = matcher.group(4).substring(repeatLength);

                matcher = pattern.matcher(input);

                result += textBeforePattern.length() + (repeatLength*repeatNumber);

            }

            result += input.length();        

        }

        return Integer.toString(result);

    }

    public static String Problem2()
    {

        InputStream inputStream = AoC2016_Day9.class.getResourceAsStream("AoC2016_Day9_input.txt");
        long result = 0;

        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {

            String input = sc.next();

            Queue<Pair<String, Integer>> queue = new LinkedList<>();

            queue.add(new Pair<>(input, 1));

            while (!queue.isEmpty()){

                Pair<String, Integer> tupleData = queue.remove();

                String stringData = tupleData.getValue0();
                int stringRepetitionFold = tupleData.getValue1();

                Pattern pattern = Pattern.compile("(^.*?)\\((\\d+)x(\\d+)\\)(.+)");
                Matcher matcher = pattern.matcher(stringData);

                if (matcher.find()){
                    
                    String textBeforePattern = matcher.group(1);

                    int repeatLength = Integer.parseInt(matcher.group(2));
                    int repeatNumber = Integer.parseInt(matcher.group(3));

                    String toBeRepeated = matcher.group(4).substring(0,repeatLength);
                    String newInput = matcher.group(4).substring(repeatLength);

                    if (newInput.length()!=0){

                        queue.add(new Pair<>(newInput, stringRepetitionFold));

                    }

                    queue.add(new Pair<>(toBeRepeated, stringRepetitionFold*repeatNumber));

                    result += textBeforePattern.length()*stringRepetitionFold;

                }else{

                    result += stringData.length()*stringRepetitionFold;

                }
            }
        }

        return Long.toString(result);

    }
    
    public static void main(String[] args) {
        
        System.out.println("Problem1 Solution : "+ Problem1());
        System.out.println("Problem2 Solution : "+ Problem2());
        
    }
}

    