import os
import random
import shutil
import signal
import sys
import time


# ANSI escape codes (colors and cursor control)
RESET = "\x1b[0m"
GREEN = "\x1b[32m"
BRIGHT_GREEN = "\x1b[92m"
DIM_GREEN = "\x1b[2;32m"
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
CLEAR = "\x1b[2J"


def move_cursor(row: int, col: int) -> str:
    return f"\x1b[{row};{col}H"


def safe_write(s: str) -> None:
    try:
        sys.stdout.write(s)
        sys.stdout.flush()
    except Exception:
        # In case the terminal can't render something, ignore to keep animation smooth
        pass


def typing_line(text: str, delay: float = 0.02) -> None:
    for ch in text:
        safe_write(ch)
        time.sleep(delay)
    safe_write("\n")


def typing_intro() -> None:
    cols, _ = shutil.get_terminal_size(fallback=(80, 24))
    banner = "// ACCESS NODE: OMEGA-GATEWAY"
    under = "=" * min(len(banner), cols)
    safe_write(BRIGHT_GREEN + banner[:cols] + RESET + "\n")
    safe_write(DIM_GREEN + under + RESET + "\n\n")

    steps = [
        "Initializing secure link...",
        "Negotiating ciphersuite [AES-256/GCM]...",
        "Syncing time with NTP shadows...",
        "Bypassing deep packet inspection...",
        "Injecting ephemeral keys...",
        "Access granted. Welcome, Operative."
    ]

    for s in steps:
        typing_line(GREEN + s + RESET, delay=0.015)
        time.sleep(0.25)

    safe_write("\n")
    time.sleep(0.5)


def matrix_rain() -> None:
    # Prepare screen
    safe_write(HIDE_CURSOR + CLEAR)

    # Graceful exit on Ctrl+C
    def handle_sigint(_sig, _frm):
        restore_terminal()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_sigint)

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@$%#*+-/\\|"  # keep ASCII for wide compatibility

    while True:
        cols, rows = shutil.get_terminal_size(fallback=(80, 24))
        # Keep a drop per column
        drops = [random.randint(-rows, 0) for _ in range(max(1, cols))]

        # Run frames until a resize happens
        target_frames_before_resize_check = 300
        frames = 0

        while frames < target_frames_before_resize_check:
            # Random jitter to avoid flat look
            for x in range(1, cols + 1):
                y = drops[x - 1]

                # Trail positions
                head = y
                mid = y - 1
                tail = y - 6

                # Draw head (bright), mid (dim), erase tail
                if 1 <= head <= rows:
                    safe_write(move_cursor(head, x) + BRIGHT_GREEN + random.choice(chars) + RESET)
                if 1 <= mid <= rows:
                    safe_write(move_cursor(mid, x) + DIM_GREEN + random.choice(chars) + RESET)
                if 1 <= tail <= rows:
                    safe_write(move_cursor(tail, x) + " ")

                # Advance this drop
                drops[x - 1] += random.choice([0, 1, 1])

                # Reset drop when off-screen with some randomness for variation
                if drops[x - 1] > rows + random.randint(0, 10):
                    drops[x - 1] = random.randint(-rows // 3, 0)

            frames += 1
            time.sleep(0.03)

        # After several frames, re-evaluate size (to handle terminal resize smoothly)


def restore_terminal() -> None:
    try:
        safe_write(RESET + SHOW_CURSOR + move_cursor(9999, 1))
    except Exception:
        pass


def main() -> None:
    try:
        typing_intro()
        matrix_rain()
    finally:
        restore_terminal()


if __name__ == "__main__":
    main()


