package com.github.alexmovsess.practice.AdventOfCode2016.Day1;

import java.io.InputStream;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.awt.geom.Point2D;

public class AoC2016_Day1 {

    public static int Problem1()
    {
        InputStream inputStream = AoC2016_Day1.class.getResourceAsStream("AoC2016_Day1_input.txt");
        try (Scanner sc = new Scanner(inputStream).useDelimiter(", ")){

            int direction = 0;
            int[] resultList = {0,0,0,0};

            while (sc.hasNext()){

                String input = sc.next();
                String[] inputSplit = { input.substring(0, 1), input.substring(1) };

                if (inputSplit[0].equals("R")){
                    direction +=1;
                    if(direction == 4){
                        direction = 0;
                    }
                } else {
                    direction-=1;
                    if (direction == -1) {
                        direction = 3;
                    }
                }
                resultList[direction]+=Integer.parseInt(inputSplit[1]);
            }
            return Math.abs(resultList[0]-resultList[2])+Math.abs(resultList[1]-resultList[3]);
        }
        
    }

    @SuppressWarnings("resource")
    public static int Problem2() throws Exception{
        InputStream inputStream = AoC2016_Day1.class.getResourceAsStream("AoC2016_Day1_input.txt");
        
        try (Scanner sc = new Scanner(inputStream).useDelimiter(", ")){
            int direction = 0;
            Point2D position = new Point2D.Double(0,0); 
            Set<Point2D> visited = new HashSet<>();
            int result = 0;
            visited.add(position);
            while (sc.hasNext()){

                String input = sc.next();
                String[] inputSplit = { input.substring(0, 1), input.substring(1) };

                if (inputSplit[0].equals("R")){
                    direction +=1;
                    if(direction == 4){
                        direction = 0;
                    }
                } else {
                    direction-=1;
                    if (direction == -1) {
                        direction = 3;
                    }
                }            
                if (direction == 0){
                    for (int i=0; i < Integer.parseInt(inputSplit[1]); i++) {
                        position.setLocation(position.getX(), position.getY()+1);
                        if (visited.contains(position) && result == 0){
                            return (int)(Math.abs(position.getX())+Math.abs(position.getY()));
                        }else{
                            visited.add(new Point2D.Double(position.getX(),position.getY()));
                        };
                    }
                } else if (direction == 1){
                    for (int i=0; i < Integer.parseInt(inputSplit[1]); i++) {
                        position.setLocation(position.getX()+1, position.getY());
                        if (visited.contains(position)){
                            return (int)(Math.abs(position.getX())+Math.abs(position.getY()));
                        }else{
                            visited.add(new Point2D.Double(position.getX(),position.getY()));
                        };
                    }
                } else if (direction == 2){
                    for (int i=0; i < Integer.parseInt(inputSplit[1]); i++) {
                        position.setLocation(position.getX(), position.getY()-1);
                        if (visited.contains(position)){
                            
                            return (int)(Math.abs(position.getX())+Math.abs(position.getY()));
                        }else{
                            visited.add(new Point2D.Double(position.getX(),position.getY()));
                        };
                    }
                } else {
                    for (int i=0; i < Integer.parseInt(inputSplit[1]); i++) {
                        position.setLocation(position.getX()-1, position.getY());
                        if (visited.contains(position)){
                            return (int)(Math.abs(position.getX())+Math.abs(position.getY()));
                        }else{
                            visited.add(new Point2D.Double(position.getX(),position.getY()));
                        };
                    }
                }
            }
            sc.close();
        }
        throw new Exception("Reached end of input without finding a solution");
    }

    public static void main(String[] args) throws Exception{
        System.out.println("Problem1 Solution : "+Problem1());
        System.out.println("Problem2 Solution : "+Problem2());
    }
}