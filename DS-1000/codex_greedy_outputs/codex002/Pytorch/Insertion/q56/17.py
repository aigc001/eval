
# Convert the mask to boolean
boolean_mask = mask.bool()

# Expand the dimensions of boolean mask to match the dimensions of output
expanded_boolean_mask = boolean_mask.unsqueeze(2).expand_as(output)

# Use the expanded boolean mask to select values from clean_input_spectrogram and output
result = torch.where(expanded_boolean_mask, clean_input_spectrogram, output)
