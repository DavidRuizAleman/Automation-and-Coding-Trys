import { test, expect } from '@playwright/test';


test('checkboxes', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');

  // Click the Checkboxes link.
  await page.getByRole('link', { name: 'Checkboxes' }).click();

  // Expects page to have a heading with the name of Installation.
  
  await expect(page.getByRole('heading', { name: 'Checkboxes'})).toBeVisible();
  page.getByRole('checkbox').first().click();

  

});


