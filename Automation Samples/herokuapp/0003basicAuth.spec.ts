import { test, expect } from '@playwright/test';
test.use({httpCredentials : {username : 'admin', password : 'admin'}});

  
test('basic Authentification', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Basic Auth link.
  await page.getByRole('link', { name: 'Basic Auth' }).click();
  await page.waitForTimeout(30);
  

  
  await expect(page.getByRole('heading', { name: 'Basic Auth'})).toBeVisible();
  
  
  
  await page.waitForTimeout(30);
  

  
  
});