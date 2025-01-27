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
  
  let links = [  'home' ,  'about',   'contact us',   'gallery',   'portfolio', 'cloud']
  let num=0
  
	links.forEach(function (value) {
		try{
			page.getByRole('link', { name: value}).toBeVisible()
				num++;
		}
		catch(e){
			console.log("Element not found: "  + value);
		}
		

		
	})
	
});