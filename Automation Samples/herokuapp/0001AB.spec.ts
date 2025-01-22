import { test, expect } from '@playwright/test';


test('load page ab', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');

  // Click the ab testing link.
  await page.getByRole('link', { name: 'A/B Testing' }).click();

  // Expects page to have a heading with the name of Installation.
  const headerOne = page.getByRole('heading', { name: 'A/B Test Control' });
  const headerTwo = page.getByRole('heading', { name: 'A/B Test Variation 2'});
  const headerThree = page.getByRole('heading', { name:'A/B Test Variation 1'});
  
  await expect(page.getByRole('heading', { name: 'A/B Test'})).toBeVisible();
  await expect((headerOne.or(headerTwo)).or(headerThree)).toBeVisible();
  
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Control');
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Variation 1');
//  await expect.soft(page.getByRole('heading')).toHaveText('A/B Test Variation 2');
  
  
  //A/B Test Control
  //A/B Test Variation 1
  //A/B Test Variation 2
  //await expect(page.getByText('A/B Test Variation')).toBeVisible();
});


