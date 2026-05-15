package com.github.alexmovsess.practice.AdventOfCode2016.Day5;

import java.io.InputStream;
import java.math.BigInteger;
import java.util.Scanner;
import java.security.*;

public class AoC2016_Day5 {
    public static String Problem1(){
        InputStream inputStream = AoC2016_Day5.class.getResourceAsStream("AoC2016_Day5_input.txt");
        String result = "";
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int index = 0;             
            String input = sc.next();
            while (result.length()!= 8){
                String hashtext = stringToHex(input + Integer.toString(index));
                if (hashtext.substring(0, 5).equals("00000")){
                    result += hashtext.substring(5, 6);
                    System.out.println("Decyphering : " + result);
                }
                index+=1;
            }
  
        }
        return result;
    }

    public static String stringToHex(String input) {
        try {

            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);

            String hashtext = no.toString(16);
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
            return hashtext;
        }
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static String Problem2(){
        InputStream inputStream = AoC2016_Day5.class.getResourceAsStream("AoC2016_Day5_input.txt");
        char[] result = {'_','_','_','_','_','_','_','_'};
        try (Scanner sc = new Scanner(inputStream).useDelimiter("\n")) {
            int index = 0;             
            String input = sc.next();
            while (new String(result).contains("_")){
                String hashtext = stringToHex(input + Integer.toString(index));
                if (hashtext.substring(0, 5).equals("00000") && "01234567".contains(hashtext.substring(5, 6))){
                    if(result[Integer.parseInt(hashtext.substring(5, 6))]=='_'){
                        result[Integer.parseInt(hashtext.substring(5, 6))] = hashtext.substring(6, 7).charAt(0);;
                        System.out.println("Decyphering : " +new String(result));
                    }
                }
                index+=1;
            }
  
        }
        return new String(result);
    }


    public static void main(String[] args) {
        System.out.println("Problem1 Solution : "+ Problem1());
        System.out.println("Problem2 Solution : "+ Problem2());
    }  
}
