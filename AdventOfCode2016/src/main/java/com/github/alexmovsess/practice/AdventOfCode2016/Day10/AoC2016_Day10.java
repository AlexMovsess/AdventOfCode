package com.github.alexmovsess.practice.AdventOfCode2016.Day10;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.javatuples.Pair;

public class AoC2016_Day10 {
    
    public static String Problem1()
    {

        InputStream inputStream = AoC2016_Day10.class.getResourceAsStream("AoC2016_Day10_input.txt");
        int result = 0;
        
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {

            Map<Integer,List<Integer>> instructionDict = new Hashtable<>();
            Map<Integer, List<Integer>> botDict = new Hashtable<>();

            while (sc.hasNext()){

                String input = sc.next();
                
                Pattern pattern = Pattern.compile("bot (\\d+) gives low to (\\w+) (\\d+) and high to (\\w+) (\\d+)|value (\\d+) goes to bot (\\d+)");
                Matcher matcher = pattern.matcher(input);

                if (matcher.find()){

                    String group1 = matcher.group(1);
                    
                    String group2 = matcher.group(2);
                    String group3 = matcher.group(3);

                    String group4 = matcher.group(4);
                    String group5 = matcher.group(5);

                    String group6 = matcher.group(6);
                    String group7 = matcher.group(7);

                    if(Objects.nonNull(group1)){

                        int givingBot = Integer.parseInt(group1);
                        String lowType = group2;
                        int lowTypeNumber = Integer.parseInt(group3);
                        String highType = group4;
                        int highTypeNumber = Integer.parseInt(group5);

                        if(!lowType.equals("bot")){
                            lowTypeNumber = -1;
                        }
                        if(!highType.equals("bot")){
                            highTypeNumber = -1;
                        }

                        instructionDict.put(givingBot, new ArrayList<Integer>(Arrays.asList(lowTypeNumber, highTypeNumber)));

                    } else {

                        int valueReceivedByBot = Integer.parseInt(group6);
                        int receivingBot = Integer.parseInt(group7);

                        if (botDict.get(receivingBot) != null){

                            botDict.get(receivingBot).add(valueReceivedByBot);

                        }else{

                            botDict.put(receivingBot, new ArrayList<Integer>(Arrays.asList(valueReceivedByBot)));

                        }

                    }

                }

            }

            while(!botDict.isEmpty()){

                for (int key : botDict.keySet()) {

                    if (botDict.get(key).size() == 2){

                        List<Integer> dispatchList = botDict.remove(key);
                        List<Integer> receivingBotList = instructionDict.get(key);

                        int botMin = receivingBotList.get(0);
                        int botMax = receivingBotList.get(1);
                        
                        int valueMin = Collections.min(dispatchList);
                        int valueMax = Collections.max(dispatchList);

                        if (valueMin == 17 && valueMax == 61){
                            result= key;
                        }

                        if (botMin != -1){
                            if (botDict.get(botMin) != null){
                                botDict.get(botMin).add(valueMin);
                            }else{
                                botDict.put(botMin, new ArrayList<Integer>(Arrays.asList(valueMin)));
                            }
                        }
                        if (botMax != -1){
                            if (botDict.get(botMax) != null){
                                botDict.get(botMax).add(valueMax);
                            }else{
                                botDict.put(botMax, new ArrayList<Integer>(Arrays.asList(valueMax)));
                            }
                        }
                        break;
                    }
                }
            }

        }

        return Integer.toString(result);

    }

    public static String Problem2()
    {

        InputStream inputStream = AoC2016_Day10.class.getResourceAsStream("AoC2016_Day10_input.txt");
        int result = 1;
        
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {

            Map<Integer,List<Pair<String,Integer>>> instructionDict = new Hashtable<>();
            Map<Integer, List<Integer>> botDict = new Hashtable<>();

            while (sc.hasNext()){

                String input = sc.next();
                
                Pattern pattern = Pattern.compile("bot (\\d+) gives low to (\\w+) (\\d+) and high to (\\w+) (\\d+)|value (\\d+) goes to bot (\\d+)");
                Matcher matcher = pattern.matcher(input);

                if (matcher.find()){

                    String group1 = matcher.group(1);
                    
                    String group2 = matcher.group(2);
                    String group3 = matcher.group(3);

                    String group4 = matcher.group(4);
                    String group5 = matcher.group(5);

                    String group6 = matcher.group(6);
                    String group7 = matcher.group(7);

                    if(Objects.nonNull(group1)){

                        int givingBot = Integer.parseInt(group1);
                        String lowType = group2;
                        int lowTypeNumber = Integer.parseInt(group3);
                        String highType = group4;
                        int highTypeNumber = Integer.parseInt(group5);

                        instructionDict.put(givingBot, new ArrayList<Pair<String,Integer>>(Arrays.asList(new Pair<String,Integer>(lowType, lowTypeNumber),new Pair<String,Integer>(highType, highTypeNumber))));

                    } else {

                        int valueReceivedByBot = Integer.parseInt(group6);
                        int receivingBot = Integer.parseInt(group7);

                        if (botDict.get(receivingBot) != null){

                            botDict.get(receivingBot).add(valueReceivedByBot);

                        }else{

                            botDict.put(receivingBot, new ArrayList<Integer>(Arrays.asList(valueReceivedByBot)));

                        }

                    }

                }

            }

            while(!botDict.isEmpty()){

                for (int key : botDict.keySet()) {

                    if (botDict.get(key).size() == 2){

                        List<Integer> dispatchList = botDict.remove(key);
                        List<Pair<String,Integer>> receivingBotList = instructionDict.get(key);

                        Pair<String,Integer> lowBranch = receivingBotList.get(0);
                        Pair<String,Integer> highBranch = receivingBotList.get(1);

                        int valueMin = Collections.min(dispatchList);
                        int valueMax = Collections.max(dispatchList);

                        int botMin = receivingBotList.get(0).getValue1();
                        int botMax = receivingBotList.get(1).getValue1();

                        if (lowBranch.getValue0().equals("output")){

                            if(lowBranch.getValue1()==0){

                                result *= valueMin;

                            }else if(lowBranch.getValue1()==1){

                                result *= valueMin;

                            }else if(lowBranch.getValue1()==2){

                                result *= valueMin;

                            }

                        }else{

                            if (botDict.get(botMin) != null){

                                botDict.get(botMin).add(valueMin);

                            }else{

                                botDict.put(botMin, new ArrayList<Integer>(Arrays.asList(valueMin)));

                            }
                        }

                        if (highBranch.getValue0().equals("output")){

                            if(highBranch.getValue1()==0){

                                result *= valueMax;

                            }else if(highBranch.getValue1()==1){

                                result *= valueMax;

                            }else if(highBranch.getValue1()==2){

                                result *= valueMax;

                            }

                        }else{

                            if (botDict.get(botMax) != null){

                                botDict.get(botMax).add(valueMax);

                            }else{

                                botDict.put(botMax, new ArrayList<Integer>(Arrays.asList(valueMax)));

                            }

                        }
                        
                        break;
                        
                    }
                }
            }

        }

        return Integer.toString(result);

    }


    public static void main(String[] args) {
        
        System.out.println("Problem1 Solution : "+ Problem1());
        System.out.println("Problem2 Solution : "+ Problem2());

      }
}

