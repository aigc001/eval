
# Convert mask to boolean tensor
mask = mask.type(torch.bool)

# Expand dimensions of mask to match output
mask = mask.unsqueeze(2).expand_as(output)

# Use mask to select values from clean_input_spectrogram and output
result = torch.where(mask, clean_input_spectrogram, output)
