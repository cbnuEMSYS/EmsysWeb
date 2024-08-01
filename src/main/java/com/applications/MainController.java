package com.applications;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

public class MainController {

    @GetMapping("/") // localhost:8080/
    public String main() {
        return ""
    }
}
