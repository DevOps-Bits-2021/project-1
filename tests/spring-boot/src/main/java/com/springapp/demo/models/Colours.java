package com.springapp.demo.models;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;




@Entity
@Table(name = "`Colours`")
public class Colours {


    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    public Long id;

    @Column(name ="name")
    private String colourName;

    @Column(name="category")
    private String category;

    @Column(name ="type")
    private String type;

    @Column(name ="code")
    private String code;

    @Column(name ="hex_code")
    private String hex_code;

    @Column(name ="frequency")
    private String frequency;



    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getColourName() {
        return colourName;
    }

    public void setColourName(String name) {
        this.colourName = name;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getHex_code() {
        return hex_code;
    }

    public void setHex_code(String hex_code) {
        this.hex_code = hex_code;
    }

    public String getFrequency() {
        return frequency;
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }






}
