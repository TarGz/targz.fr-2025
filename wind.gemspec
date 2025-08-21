# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "wind"
  spec.version       = "0.1.0"
  spec.authors       = ["Targz"]
  spec.email         = ["hello@targz.fr"]

  spec.summary       = "A minimal Jekyll theme for targz.fr portfolio"
  spec.homepage      = "https://targz.fr"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.3"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.8"
  spec.add_runtime_dependency "webrick", "~> 1.8"
end