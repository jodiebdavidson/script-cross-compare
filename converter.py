require 'csv'
require 'json'

def convert_csv_to_json(csv_file, json_file)
  csv_data = CSV.read(csv_file, headers: true).map(&:to_h)
  
  File.open(json_file, "w") do |f|
    f.write(JSON.pretty_generate(csv_data))
  end
  puts "Ruby: Conversion Complete!"
end

# Usage
# convert_csv_to_json('data.csv', 'data.json')
