package com.github.alexmovsess.practice.AdventOfCode2016.Day7;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AoC2016_Day7 {
    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day7.class.getResourceAsStream("AoC2016_Day7_input.txt");
        int result = 0;
        try (Scanner sc = new Scanner(inputStream)) {
            while (sc.hasNext()){

                String input = sc.next();
                Boolean outsideBracketsContainsABBA = false;
                Boolean insideBracketsContainsABBA = false;

                Pattern patternOutsideBrackets = Pattern.compile("(\\w+)(?:\\[\\w+\\])?");
                Matcher matcherOutsideBrackets = patternOutsideBrackets.matcher(input);
                while (matcherOutsideBrackets.find()){
                    if(findABBA(matcherOutsideBrackets.group(1))){
                        outsideBracketsContainsABBA = true;
                    }
                }

                Pattern patternInsideBrackets = Pattern.compile("\\[(\\w+)\\]?");
                Matcher matcherInsideBrackets = patternInsideBrackets.matcher(input);
                while (matcherInsideBrackets.find()){
                    if(findABBA(matcherInsideBrackets.group(1))){
                        insideBracketsContainsABBA = true;
                    }
                }

                if(outsideBracketsContainsABBA && !insideBracketsContainsABBA){
                    result +=1;
                }
            }
        }
        return Integer.toString(result);
    }

    public static Boolean findABBA(String str){
        for (int i =0; i< str.length()-3;i++){
            if(str.charAt(i) == str.charAt(i+3) && str.charAt(i+1) == str.charAt(i+2) && str.charAt(i) != str.charAt(i+1)){
                return true;
            }
        }
        return false;
    }

    public static String Problem2()
    {
        InputStream inputStream = AoC2016_Day7.class.getResourceAsStream("AoC2016_Day7_input.txt");
        int result = 0;
        try (Scanner sc = new Scanner(inputStream)) {
            while (sc.hasNext()){

                String input = sc.next();

                Boolean ABACondition = false;

                Pattern patternOutsideBrackets = Pattern.compile("(\\w+)(?:\\[\\w+\\])?");
                Matcher matcherOutsideBrackets = patternOutsideBrackets.matcher(input);
                List<String> listOutsideBrackets = new ArrayList<String>();
                while (matcherOutsideBrackets.find()){
                    listOutsideBrackets.addAll(findABA(matcherOutsideBrackets.group(1)));
                }

                Pattern patternInsideBrackets = Pattern.compile("\\[(\\w+)\\]?");
                Matcher matcherInsideBrackets = patternInsideBrackets.matcher(input);
                List<String> listInsideBrackets = new ArrayList<String>();
                while (matcherInsideBrackets.find()){
                    listInsideBrackets.addAll(findABA(matcherInsideBrackets.group(1)));
                }

                for(int i =0; i<listOutsideBrackets.size();i++){
                    for (int j =0; j<listInsideBrackets.size();j++){
                        if(listOutsideBrackets.get(i).charAt(0) == listInsideBrackets.get(j).charAt(1) 
                        && listOutsideBrackets.get(i).charAt(1) == listInsideBrackets.get(j).charAt(0)){
                            ABACondition = true;
                        }
                    }
                }

                if(ABACondition){
                    result +=1;
                }
            }
        }
        return Integer.toString(result);
    }

    public static List<String> findABA(String str){
        List<String> result = new ArrayList<String>();
        for (int i =0; i< str.length()-2;i++){
            if(str.charAt(i) == str.charAt(i+2) && str.charAt(i) != str.charAt(i+1)){
                result.add(str.substring(i, i+3));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+ Problem1());
        System.out.println("Problem2 Solution : "+ Problem2());
    } 
}
