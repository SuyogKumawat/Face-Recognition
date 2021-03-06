provider "aws"{
region="ap-south-1"
access_key=#ACCESS KEY
secret_key=#Secret Key
}

resource "aws_instance" "os1"{
ami="ami-0ad704c126371a549"
instance_type="t2.micro"
tags= {
   Name="mlops instance"
   }
}

resource "aws_ebs_volume" "ebs1"{
    availability_zone=aws_instance.os1.availability_zone
    size=5

    tags={
        Name="ebs-volume"
    }
}

resource "aws_volume_attachment" "at"{
    device_name="/dev/sdh"
    volume_id=aws_ebs_volume.ebs1.id
    instance_id=aws_instance.os1.id
}
