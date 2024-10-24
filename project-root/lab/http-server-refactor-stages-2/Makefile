# Compiler and linker settings
ASSEMBLER := as
LINKER := ld
CC := gcc
ARCH := arm64

# Flags
CFLAGS := -c -g
ASMFLAGS := -arch $(ARCH) -g
LDFLAGS := -l System -syslibroot $$(xcrun -sdk macosx --show-sdk-path) -e _main -arch $(ARCH) -v

# Directories
SRC_DIR := src
OBJ_DIR := obj
BIN_DIR := bin

# Target binary
BIN := server
TARGET := $(BIN_DIR)/$(BIN)

# Source files
ASM_SRCS := $(shell find $(SRC_DIR) -name '*.s')
C_SRCS := $(shell find $(SRC_DIR) -name '*.c')

# Object files
ASM_OBJS := $(patsubst $(SRC_DIR)/%.s,$(OBJ_DIR)/%.o,$(ASM_SRCS))
C_OBJS := $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(C_SRCS))
ALL_OBJS := $(ASM_OBJS) $(C_OBJS)

# Ensure all necessary directories exist
$(shell mkdir -p $(OBJ_DIR) $(BIN_DIR) $(sort $(dir $(ALL_OBJS))))

# Targets and rules
.PHONY: all clean

all: $(TARGET)

$(TARGET): $(ALL_OBJS)
	@echo "Linking: $@"
	$(LINKER) $(LDFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.s
	@echo "Assembling: $<"
	$(ASSEMBLER) $(ASMFLAGS) -o $@ $<

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@echo "Compiling: $<"
	$(CC) $(CFLAGS) -o $@ $<

clean:
	@echo "Cleaning up..."
	rm -rf $(OBJ_DIR) $(BIN_DIR)
