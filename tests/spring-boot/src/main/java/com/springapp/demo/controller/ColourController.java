package com.springapp.demo.controller;


import com.springapp.demo.models.Colours;
import com.springapp.demo.repository.ColoursRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.NoSuchElementException;

@RestController
public class ColourController {

    @Autowired
    private ColoursRepository coloursRepository;

    @CrossOrigin(origins = "http://localhost:8080")
    @GetMapping("/colours")
    public List<Colours> getColours() {
        return coloursRepository.findAll();
    }

    @CrossOrigin(origins = "http://localhost:8080")
    @GetMapping("/colour/{name}")
    public Colours getColour(@PathVariable String name)
    throws NoSuchElementException
    {
        return coloursRepository.findByColourName(name);
    }
}
