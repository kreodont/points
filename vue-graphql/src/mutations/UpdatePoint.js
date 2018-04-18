import gql from 'graphql-tag'

export default gql`
    mutation updatePoint($id: ID!, $expectedVersion: Int, $number: Int, $points_owner_id: String, $details: String)
      {
        updatePoint(input: {id: $id, expectedVersion: $expectedVersion, number: $number})
        {details}

      }
    `
