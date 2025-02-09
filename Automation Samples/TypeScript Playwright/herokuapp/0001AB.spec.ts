import { test, expect } from '@playwright/test';
//Test configurations

//Imports, test for the test locations and executions.
//Imports, expect is for assertions.
//Other possible values:
//defineConfig, devices, ElementHandle, etc

//High Level Test Strategy:
//Save all possible outcomes to constant, ensure that one of them is visible on load. 
test('load page ab', async ({ page }) => {
  //Load the base page.
  await page.goto('https://the-internet.herokuapp.com');

  // Click the ab testing link.
  await page.getByRole('link', { name: 'A/B Testing' }).click();

  // Expects page to have a heading with one of the possible headings
  const header1 = page.getByRole('heading', { name: 'A/B Test Control' });
  const header2 = page.getByRole('heading', { name: 'A/B Test Variation 2'});
  const header3 = page.getByRole('heading', { name: 'A/B Test Variation 1'});
  
  await expect(page.getByRole('heading', { name: 'A/B Test'})).toBeVisible();
  //General test case to ensure that we are a) on the correct page, and b) it has loaded properly
  await expect((header1.or(header2)).or(header3)).toBeVisible();
  //Or with all 3 posibilites to ensure one of them is covered. 
  //Changed variable names from headerOne to header1 for readability and scallability. 

// Original idea was to do soft assertions to get one past. 
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Control');
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Variation 1');
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Variation 2');
  
//Possible text on screen are: 
  //A/B Test Control
  //A/B Test Variation 1
  //A/B Test Variation 2
});


