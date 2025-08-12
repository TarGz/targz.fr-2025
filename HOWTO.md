 You need a newer Ruby version. Install it with Homebrew:

  # Install Homebrew if you don't have it
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  # Install rbenv and ruby-build
  brew install rbenv ruby-build

  # Install Ruby 3.2
  rbenv install 3.2.2
  rbenv global 3.2.2

  # Add rbenv to your shell
  echo 'eval "$(rbenv init -)"' >> ~/.zshrc
  source ~/.zshrc

  # Then reinstall bundle
  gem install bundler
  bundle install
  bundle exec jekyll serve


bundle exec jekyll serve
bundle exec jekyll serve --livereload
