package com.github.alexmovsess.practice.AdventOfCode2016.Day2;

import java.io.InputStream;
import java.util.Scanner;

public class AoC2016_Day2 {

    public static String Problem1()
    {
        InputStream inputStream = AoC2016_Day2.class.getResourceAsStream("AoC2016_Day2_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int keypad[][] ={{ 1, 2, 3 },
                            { 4, 5, 6 },
                            { 7, 8, 9 }};
            int x = 1;
            int y = 1;
            String result = "";
            while (sc.hasNext()){
                String input =  sc.next();
                for (int i = 0; i < input.length(); i++){
                    char c = input.charAt(i); 
                    if (c == 'U') {
                        if (y > 0){
                            y-=1;
                        }
                    } else if (c == 'R'){
                        if (x < 2){
                            x+=1;
                        }
                    } else if (c == 'D'){
                        if (y < 2){
                            y+=1;
                        }
                    } else if (c == 'L') {
                        if (x > 0){
                            x-=1;
                        }
                    }
                    
                }
                result += keypad[y][x];
            }
            return result;
        } 
    }

    public static String Problem2()
    {
        InputStream inputStream = AoC2016_Day2.class.getResourceAsStream("AoC2016_Day2_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int keypad[][] ={   { -1, -1, 1, -1, -1 },
                                { -1, 2, 3, 4, -1 },
                                { 5, 6, 7, 8, 9 },
                                { -1, 'A', 'B', 'C', -1 },
                                { -1, -1, 'D', -1, -1 }};
            int x = 0;
            int y = 2;
            String result = "";
            while (sc.hasNext()){
                String input =  sc.next();
                for (int i = 0; i < input.length(); i++){
                    char c = input.charAt(i); 
                    if (c == 'U') {
                        if (y > 0 && keypad[y-1][x] != -1){
                            y-=1;
                        }
                    } else if (c == 'R'){
                        if (x < 4 &&  keypad[y][x+1] != -1){
                            x+=1;
                        }
                    } else if (c == 'D'){
                        if (y < 4 && keypad[y+1][x] != -1){
                            y+=1;
                        }
                    } else if (c == 'L') {
                        if (x > 0 && keypad[y][x-1] != -1){
                            x-=1;
                        }
                    }
                    
                }
                if (keypad[y][x]<65){
                    result += keypad[y][x];
                }else{
                    result += (char) keypad[y][x];
                }
            }
            return result;
        }

    } 
    
    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+Problem1());
        System.out.println("Problem2 Solution : "+Problem2());
    }   
}
