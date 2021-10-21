package com.springapp.demo;


import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class DemoApplicationTests {

	WebDriver driver;
	  private Map<String, Object> vars;
	  JavascriptExecutor js;
	  
	  String url = "http://ec2-3-22-95-211.us-east-2.compute.amazonaws.com:8080/";
	  String username = "username";
	  String password = "password";
	  
	
	  
	  
	@Before
    public  void setup() {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\I513949\\Downloads\\chromedriver_win32\\chromedriver.exe");
		driver = new ChromeDriver();
		 vars = new HashMap<String, Object>();
		  js = (JavascriptExecutor) driver;
		
    }
	
	/*
	 * Login Page
	 */
	
	 @Test
	  public void testIfLoginPageOpens() {

		  driver.get("http://ec2-3-22-95-211.us-east-2.compute.amazonaws.com:8080/");
		    driver.manage().window().setSize(new Dimension(1296, 736));
		    driver.findElement(By.linkText("Login")).click();
		    String ActualTitle = driver.getTitle();
		    Assert.assertEquals("Login", ActualTitle);
			 driver.quit();
	   
	  }
	 
	 @Test
	  public void login() {
		 driver.get("http://ec2-3-22-95-211.us-east-2.compute.amazonaws.com:8080/");
		    driver.manage().window().setSize(new Dimension(1296, 736));
		    driver.findElement(By.linkText("Login")).click();
		    driver.findElement(By.id(username)).click();
		    driver.findElement(By.id(username)).sendKeys("testUser");
		    driver.findElement(By.id(password)).sendKeys("testUser");
		    driver.findElement(By.cssSelector("body")).click();
		    driver.findElement(By.id("submit")).click();
		    driver.findElement(By.linkText("Logout")).click();
		    WebElement we = driver.findElement(By.linkText("Login"));
		    driver.quit();
		    Assert.assertNotEquals(we, null);
		    
		    
	  }
	 /*
	  * Login Page ends
	  */
	 
	 /*
	  * Add new recipe
	  */
	 
	 @Test
	  public void addNewRecipe() {
	    driver.get("http://ec2-3-22-95-211.us-east-2.compute.amazonaws.com:8080/");
	    driver.manage().window().setSize(new Dimension(1296, 736));
	    driver.findElement(By.linkText("Login")).click();
	    driver.findElement(By.id(username)).click();
	    driver.findElement(By.id(username)).sendKeys("testUser");
	    driver.findElement(By.cssSelector(".form-group:nth-child(6)")).click();
	    driver.findElement(By.id(password)).sendKeys("testUser");
	    driver.findElement(By.cssSelector("form")).click();
	    driver.findElement(By.id("submit")).click();
	    driver.findElement(By.linkText("Recipe Book")).click();
	    driver.findElement(By.linkText("Add New Recipe")).click();
	    driver.findElement(By.id("name")).click();
	    driver.findElement(By.id("name")).sendKeys("Paneer Tikka");
	    driver.findElement(By.id("ingredients")).click();
	    driver.findElement(By.id("ingredients")).sendKeys("Cottage Cheese, Turmeric, Garlic");
	    driver.findElement(By.id("instructions")).click();
	    driver.findElement(By.id("instructions")).sendKeys("Loreum epsum");
	    driver.findElement(By.id("submit")).click();
	  WebElement we =  driver.findElement(By.className("recipe-page"));
	    driver.findElement(By.linkText("Logout")).click();
	    driver.quit();
	    Assert.assertNotEquals(we, null);
	  }
	 
	 
	 /*
	  * 
	  * Discover
	  */
	 
	 @Test
	  public void discover() {
	    driver.get("http://ec2-3-22-95-211.us-east-2.compute.amazonaws.com:8080/");
	    driver.manage().window().setSize(new Dimension(1296, 736));
	    driver.findElement(By.linkText("Login")).click();
	    driver.findElement(By.id(username)).click();
	    driver.findElement(By.id(username)).sendKeys("testUser");
	    driver.findElement(By.id(password)).sendKeys("testUser");
	    driver.findElement(By.cssSelector(".form-group:nth-child(6)")).click();
	    driver.findElement(By.id("submit")).click();
	    driver.findElement(By.linkText("Discover")).click();
	    driver.findElement(By.cssSelector(".col-12:nth-child(4) .post-tag")).click();
	    driver.findElement(By.linkText("Healthy Food")).click();
	    String ActualTitle = driver.getTitle();
	    driver.quit();
	    Assert.assertEquals(ActualTitle, "50 Foods That Are Super Healthy");
	    
	    
	  }




	 
	
	
	

}

