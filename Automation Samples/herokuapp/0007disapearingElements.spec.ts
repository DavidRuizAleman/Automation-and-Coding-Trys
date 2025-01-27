import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//Log all possible values, create a loop and iterate to see if all are present. 
test('Disappearing Elements', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Disappearing Elements link.
  await page.getByRole('link', { name: 'Disappearing Elements' }).click();
  await expect(page.getByRole('heading', { name: 'Disappearing Elements'})).toBeVisible();
  
  let links = [  'home',  'about',   'contact us',   'gallery',   'portfolio']  
  
	
	links.forEach(function (value) {
		console.log("trying: "  + value);
		const current = page.getByRole('link', { name: value});
		try{
			expect.soft(page.getByRole('link',{ name: value})).toBeVisible();
		}
		catch{
			console.log("Element not found: "  + value);
			console.warn('Could not click on #may-not-exist, test will continue:', error);
		}
		
		 //if (await ) {
			 
		 
		
		if(page.getByRole('link', { name: value}).isVisible()){
			  page.waitForTimeout(3);
			console.log("Element found: "  + value);
		}
		else{
			  page.waitForTimeout(30);
			console.log("Element not found: "  + value);
			} 
			
		

		
	})
	
});