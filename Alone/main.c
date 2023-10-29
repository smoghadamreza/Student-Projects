#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <simple2d.h>

int currentPlayer;
int gameSpeed;
int player1Score;
int player2Score;
S2D_Window *window;

void initializeGame() {
    srand(time(NULL));
    currentPlayer = (rand() % 2) + 1;
    player1Score = 0;
    player2Score = 0;

    printf("Enter game speed: ");
    scanf("%d", &gameSpeed);
    if (gameSpeed < 1 || gameSpeed > 3)
        gameSpeed = 1;
}

void updateScore(int scoreChange) {
    if (currentPlayer == 1)
        player1Score += scoreChange;
    else if (currentPlayer == 2)
        player2Score += scoreChange;
}

void switchTurn() {
    currentPlayer = (currentPlayer == 1) ? 2 : 1;
}

void shoot() {
    int hitPlayer = (rand() % 2) + 1;
    int hitTarget = (hitPlayer == 1) ? 2 : 1;

    if (hitPlayer == hitTarget)
        updateScore(5);
    else if (hitPlayer == currentPlayer)
        updateScore(-3);

    if (hitPlayer == hitTarget || hitPlayer == currentPlayer)
        switchTurn();
}

void saveGame() {
    FILE* file = fopen("game.txt", "w");
    if (file != NULL) {
        fprintf(file, "%d\n", currentPlayer);
        fprintf(file, "%d\n", player1Score);
        fprintf(file, "%d\n", player2Score);
        fclose(file);
        printf("Game saved successfully.\n");
    } else {
        printf("Error: Could not save the game.\n");
    }
}

void loadGame() {
    FILE* file = fopen("game.txt", "r");
    if (file != NULL) {
        fscanf(file, "%d", &currentPlayer);
        fscanf(file, "%d", &player1Score);
        fscanf(file, "%d", &player2Score);
        fclose(file);
        printf("Game loaded successfully.\n");
    } else {
        printf("Error: Could not load the game.\n");
    }
}

void displayGameStatus() {
    printf("Current Player: Player %d\n", currentPlayer);
    printf("Player 1 Score: %d\n", player1Score);
    printf("Player 2 Score: %d\n", player2Score);
    printf("Game Speed: %d\n", gameSpeed);
}

void renderGame() {
    S2D_DrawText("Game Status:", 20, 50, 30, window->width, window->height, 1, 1, 1, 1);
    char status[100];
    sprintf(status, "Current Player: Player %d", currentPlayer);
    S2D_DrawText(status, 20, 100, 20, window->width, window->height, 1, 1, 1, 1);
    sprintf(status, "Player 1 Score: %d", player1Score);
    S2D_DrawText(status, 20, 150, 20, window->width, window->height, 1, 1, 1, 1);
    sprintf(status, "Player 2 Score: %d", player2Score);
    S2D_DrawText(status, 20, 200, 20, window->width, window->height, 1, 1, 1, 1);
    sprintf(status, "Game Speed: %d", gameSpeed);
    S2D_DrawText(status, 20, 250, 20, window->width, window->height, 1, 1, 1, 1);
}

void on_key(S2D_Event e) {
    if (e.type == S2D_KEY_DOWN) {
        if (e.key == S2D_KEY_S) {
            saveGame();
        } else if (e.key == S2D_KEY_L) {
            loadGame();
        }
    }
}

void update(void) {
    if (S2D_KEY_PRESSED(S2D_KEY_SPACE)) {
        shoot();
        displayGameStatus();
    }
}

int main() {
    window = S2D_CreateWindow("Simple2D Game", 800, 600, update, renderGame, 0);
    S2D_SetWindowIcon(window, "icon.png");
    S2D_SetKeyCallback(on_key);

    initializeGame();
    displayGameStatus();

    S2D_Show(window);
    S2D_FreeWindow(window);

    return 0;
}
