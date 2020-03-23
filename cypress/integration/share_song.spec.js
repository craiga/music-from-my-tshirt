describe("Share a song", () => {
  it("Can share a song", () => {
    cy.visit("/");
    cy.contains("Share a Song").click();
    cy.contains("label", "Email").click().type("test-user@example.com");
    cy.contains("label", "Password").click().type("test password");
    cy.contains("button", "Sign In").click();
    cy.contains("label", "Artist").click().type("Tankerville");
    cy.contains("label", "Title").click().type("Bible Bashers Hitler Youth");
    cy.contains("label", "URL")
      .click()
      .type(
        "https://tankervilleband.bandcamp.com/track/bible-bashers-hitler-youth"
      );
    cy.contains("button", "Share").click();
    cy.contains("Bible Bashers Hitler Youth by Tankerville");
  });
});
