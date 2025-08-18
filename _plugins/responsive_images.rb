require 'fileutils'

Jekyll::Hooks.register :site, :after_init do |site|
  puts "🖼️  Generating all responsive images..."
  
  source_images_dir = File.join(site.source, 'assets', 'images')
  mobile_dir = File.join(source_images_dir, 'mobile')
  tablet_dir = File.join(source_images_dir, 'tablet')
  
  # Create subdirectories if they don't exist
  FileUtils.mkdir_p(mobile_dir)
  FileUtils.mkdir_p(tablet_dir)
  
  generated_count = 0
  force_regenerate = ENV['FORCE_RESPONSIVE_IMAGES'] == 'true'
  
  # Process ALL webp images (including those with different naming patterns)
  Dir.glob(File.join(source_images_dir, '*.webp')).each do |source_image|
    basename = File.basename(source_image, '.webp')
    
    # Skip if already a responsive version
    next if basename.end_with?('-mobile', '-tablet')
    
    # Determine the base name and source image
    if basename.end_with?('-preview')
      # For hyphen preview images, strip -preview for output
      base_name = basename.sub('-preview', '')
      use_source = source_image
    elsif basename.end_with?('_preview')
      # For underscore preview images (like plasma_convection_left_preview)
      # Strip _preview to get plasma_convection_left
      base_name = basename.sub(/_preview$/, '')
      use_source = source_image
    else
      # For regular images without preview suffix
      base_name = basename
      use_source = source_image
    end
    
    # Generate mobile version in mobile/ subfolder
    mobile_path = File.join(mobile_dir, "#{base_name}.webp")
    if !File.exist?(mobile_path) || force_regenerate
      system("magick '#{use_source}' -resize 400x '#{mobile_path}'")
      puts "  ✅ Generated: mobile/#{base_name}.webp"
      generated_count += 1
    end
    
    # Generate tablet version in tablet/ subfolder
    tablet_path = File.join(tablet_dir, "#{base_name}.webp")
    if !File.exist?(tablet_path) || force_regenerate
      system("magick '#{use_source}' -resize 600x '#{tablet_path}'")
      puts "  ✅ Generated: tablet/#{base_name}.webp"
      generated_count += 1
    end
  end
  
  if generated_count > 0
    puts "✨ Generated #{generated_count} responsive images!"
    puts "📁 Images saved in assets/images/mobile/ and assets/images/tablet/"
    puts "💡 Tip: Set FORCE_RESPONSIVE_IMAGES=true to regenerate existing images"
  else
    puts "✅ All responsive images already exist"
    puts "💡 Tip: Set FORCE_RESPONSIVE_IMAGES=true to regenerate them"
  end
end