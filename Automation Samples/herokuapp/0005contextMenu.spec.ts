import { test, expect } from '@playwright/test';
test('Context Menu', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');
  // Click the Context Menu link.
  await page.getByRole('link', { name: 'Context Menu' }).click();
  await expect(page.getByRole('heading', { name: 'Context Menu'})).toBeVisible();
  //second dialog is very important. Took me an hour to find this mistake
  page.on('dialog', async dialog =>{
	  expect(dialog.type()).toContain('alert');
	  expect(dialog.message()).toContain('You selected a context menu');
    await dialog.accept();
  });
 await page.locator('#hot-spot').click({button : 'right'});
});