describe("User profile", () => {
  it("Can view song", () => {
    cy.visit("/u/test-user");
    cy.contains("label", "Email")
      .click()
      .type("test-user@example.com");
    cy.contains("label", "Password")
      .click()
      .type("test password");
    cy.contains("button", "Sign In").click();
    cy.contains("Guns Germs Steel by Hoodlum Shouts");
    cy.contains("Underwater Record Store by Penelope Isles");
    cy.should("not.contain", "Barbie Girl by Aqua");
  });
});
