import { test, expect } from '@playwright/test';


  
test('load page addRemoveelEments', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');
  //Get a random number to click
  var num = 0;
  num =  Math.floor(Math.random() * 20)
  console.log(num); 
  
  // Click the add remove element link.
  await page.getByRole('link', { name: 'Add/Remove Elements' }).click();
  await expect(page.getByRole('heading', { name: 'Add/Remove Elements'})).toBeVisible();
  
  // Click the add element N times
  for (var i = 0; i < num; i++) {
    await page.getByRole('Button', { name: 'Add Element' }).click();
	await page.waitForTimeout(3);
  }
  
  // Click the first delete element N times
  for (var i = 0; i < num; i++) {
    await page.getByRole('Button', { name: 'Delete' }).first().click();
	await page.waitForTimeout(3);
  }

  
  await page.waitForTimeout(3);
  

  
  
});