# Entity - Validation - ViewModel

## Entities - The big Picture

--- Entity keys

- Primary key : Unique Identifying Key (Ex. Id)
- Foreign Key : Attribute that connects an entity to another (Ex. ClientId)
- Natural Key: Existing, or Real World Identidier (Ex. Phone number, )

--- Navigation properties

They are .NET property object that reference a related entity. They are like relationship definition in Laravel.

--- Owning Relationship

Entity defining owning relationship, delegate extras colum or properties to other entity (Ex. Client{Address} -> Address{} )


--- Attribute Types

- Simple : Scalar types (Ex. birthday, name, etc..)

- Composite: Complex type owned by the Entity (Ex. Address of Client)

- Collections: Multi-Value attributes (Ex. List<PhoneNumbers> of Client)

### Demo code

> dotnet ef database update -> Run database migration and seeder runner

> dotnet ef migrations add SchemaChanges -p <Path> -o <OutputPath>

```cs
namespace AppNamespace.Data.Entities
{
    public class TimeBill
    {
        public int Id {get; set; }
        public DateTime WorkDate {get; set; }

        // Employee entity relationship
        public Employee Employee { get; set; }

        // Case Entity relationship
        public Case Case { get; set; }
    }

    public class Client
    {
        // Attributes or Properties definition
        // ...

        // Owned relation
        public Address Address {get; set; }

        // One-To-Many relationship
        public ICollection<Case> Cases {get; set; }
    }

    public class Case
    {
        // Attributes or Properties definition
        // ...

        // Reverse One-To-Many relationship
        public Client Client {get; set; }

    }
}
```

## Models & View Models

A use-case specific structure of data for binding to physical views, Logical views or APIs.

```cs
namespace AppNamespace.ViewModels
{
    public class ClientViewModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string ContactName { get; set; }
    }
}
```

Note: Learn more from AutoMapper for mapping purpose in future.

## Server-Side Validation

It allows to ensure that a program operate on clean, correct and useful data, checking for correctness, meaningfulness and security of input data.


```cs
// Validation at migration level

namespace AppNamespace.Database
{
    public class ApplicationDbContext : DbContext
    {
        public DbSet<Client> Clients { get; set; }
        public DbSet<Case> Cases { get; set; }

        public override void OnModelCreating(ModelBuilder b)
        {
            // Adding validation on Entity level
            b.Entity<Case>()
            .Property(c => c.FileNumber)
            // Add required attribute/Not Null constraint to file_number column
            .IsRequired()
            // Set the varchar size of the file_number column
            .HasMaxLength(50);

            b.Entity<Client>(
                t => {
                    t.HasData(new Client {
                        // Provide fields default data
                    });
                }
            );
        }
    }
}
```

--- Fluent Validation

It provides an alternative to Attribute validation.

> Requires FluentValidation package by Jeremih

```cs
using FluentValidation;

public class ViewModelClassValidator : AbstractValidator<ViewModelClass>
{
    public ViewModelClassValidator()
    {
        // Defining fluent validation
        RuleFor(c => c.FileNumber).NotEmpty()
                                .Matches(@"Regex")
                                .WithMessage("Error message");
    }

}
```

--- Async Validation