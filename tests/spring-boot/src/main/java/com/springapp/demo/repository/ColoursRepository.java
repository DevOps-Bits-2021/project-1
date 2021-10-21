package com.springapp.demo.repository;


import com.springapp.demo.models.Colours;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ColoursRepository extends JpaRepository<Colours, Long> {
    Colours findByColourName(String name);
}
