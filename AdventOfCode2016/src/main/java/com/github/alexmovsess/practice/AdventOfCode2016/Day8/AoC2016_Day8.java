package com.github.alexmovsess.practice.AdventOfCode2016.Day8;

import java.io.InputStream;
import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Objects;

public class AoC2016_Day8 {
    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day8.class.getResourceAsStream("AoC2016_Day8_input.txt");
        int[][] screen = new int[6][50];

        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            while (sc.hasNext()){
                String input = sc.next();
                
                Pattern pattern = Pattern.compile("(\\d+)x(\\d+)|(\\w)=(\\d+) by (\\d+)");
                Matcher matcher = pattern.matcher(input);

                if (matcher.find()){

                    String group1 = matcher.group(1);
                    String group2 = matcher.group(2);
                    String group3 = matcher.group(3);
                    String group4 = matcher.group(4);
                    String group5 = matcher.group(5);

                    if(Objects.nonNull(group1)){

                        int rectangleLength= Integer.parseInt(group1);
                        int rectangleHeigth= Integer.parseInt(group2);

                        for (int i=0;i<rectangleLength;i++){
                            for (int j=0;j<rectangleHeigth;j++){
                                screen[j][i] = 1;
                            }
                        }

                    }else{

                        int index= Integer.parseInt(group4);
                        int rotationValue= Integer.parseInt(group5);

                        if (!group3.equals("x")){

                            int[] copy = new int[50];
                            int i = 0;

                            while (i<50){
                                if (i + rotationValue >= 50){
                                    rotationValue -=50;
                                }
                                copy[i + rotationValue] = screen[index][i];
                                i++;
                            }

                            screen[index] = copy;

                        }else{

                            int[] copy = new int[6];
                            int i = 0;

                            while (i<6){
                                if (i + rotationValue >= 6){
                                    rotationValue -=6;
                                }
                                copy[i + rotationValue] = screen[i][index];
                                i++;
                            }

                            for (int k=0;k<6;k++){
                                screen[k][index] = copy[k];
                            }
                        }        
                    }                    
                }
            }
        }

        System.out.println("Printing final screen");
        System.out.println("");

        for (int k = 0; k<10;k++){
            System.out.println("Character "+(k+1)+" : ");
            for (int i =0; i<screen.length; i++){
                System.out.println(Arrays.toString(Arrays.copyOfRange(screen[i], k*5, (k+1)*5)));
            }
            System.out.println("");            
        }   
        
        int result = 0;

        for (int i =0; i<6; i++){
            for (int j =0; j<50; j++){
                result += screen[i][j];
            }
        }
        return Integer.toString(result);
    }
    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+ Problem1());
    } 
}
