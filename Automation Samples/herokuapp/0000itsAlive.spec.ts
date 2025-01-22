import { test, expect } from '@playwright/test';

test('its alive', async ({ page }) => {
  await page.goto('https://the-internet.herokuapp.com');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle("The Internet");
});