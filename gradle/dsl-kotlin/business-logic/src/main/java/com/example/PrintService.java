package com.example;

import org.apache.commons.lang3.StringUtils;
import org.slf4j.*;

public class PrintService {
    private static Logger logger = LoggerFactory.getLogger(PrintService.class);
    public void print(MessageModel messageModel) {
        logger.info("Printing: " + messageModel.getMessage());
        String message = StringUtils.trim(messageModel.getMessage());
        System.out.println(message);
    }
}
