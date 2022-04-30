resource "aws_vpc" "main" {
  # Referencing the base_cidr_block variable allows the network address
  # to be changed without modifying the configuration.
  instance_type = "t2.micro"
  ami           = "foo"
}
