# Compiler and linker
ASSEMBLER = as
LINKER = ld

# Directories
SRCDIR = src
OBJDIR = obj
BINDIR = bin

# Target binary
TARGET = $(BINDIR)/import-extern-test

# Find all source files (including public.s)
SRCS = $(shell find $(SRCDIR) -name '*.s')

# Generate object file names
OBJS = $(patsubst $(SRCDIR)/%.s,$(OBJDIR)/%.o,$(SRCS))

# Flags
ASFLAGS = -g
LDFLAGS = -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _main -arch arm64

# Phony targets
.PHONY: all clean

# Default target
all: $(TARGET)

# Linking
$(TARGET): $(OBJS)
	@mkdir -p $(@D)
	$(LINKER) $(LDFLAGS) -o $@ $^

# Compiling
$(OBJDIR)/%.o: $(SRCDIR)/%.s
	@mkdir -p $(@D)
	$(ASSEMBLER) $(ASFLAGS) -o $@ $<

# Clean
clean:
	rm -rf $(OBJDIR) $(BINDIR)

# Debug info
debug:
	@echo "Source files:"
	@echo $(SRCS)
	@echo "Object files:"
	@echo $(OBJS)
