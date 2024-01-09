package com.example;

import org.apache.commons.lang3.StringUtils;

import com.example.PrintService;

public class MyApplication {
    public static void main(String[] args) {
        String text = "Hi! =)";
        text  = StringUtils.capitalize(text);
        new PrintService().print(new MessageModel(text));
    }
}
