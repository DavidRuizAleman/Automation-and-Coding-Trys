import { test, expect } from '@playwright/test';
test.use({httpCredentials : {username : 'admin', password : 'admin'}});

  
test('Digsest Authentification', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');


  // Click the Basic Auth link.
  await page.getByRole('link', { name: 'Digest Authentication' }).click();
  await page.waitForTimeout(30);
  

  
  await expect(page.getByRole('heading', { name: 'Digest Auth'})).toBeVisible();
  
  
  
  await page.waitForTimeout(30);
  

  
  
});